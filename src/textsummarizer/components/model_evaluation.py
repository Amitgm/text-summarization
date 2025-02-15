
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from tqdm import tqdm
from datasets import load_from_disk
import pandas as pd
import evaluate
from src.textsummarizer.entity import ModelEvaluationConfig


class ModelEvalaution:

    def __init__(self, config: ModelEvaluationConfig):

        self.config = config

        self.device = "cuda" if torch.cuda.is_available() else "cpu"  # ✅ Define `device` here


    
    def generate_batch_sized_chunks(self,list_of_elements, batch_size):
        

        """split the dataset into smaller batches that we can process simultaneously Yield"""

        for i in range(0, len(list_of_elements), batch_size):

            yield list_of_elements[i : i + batch_size]

    def calculate_metric_on_test_ds(self,dataset, metric, model, tokenizer,batch_size=16, column_text="article",
                                    column_summary="highlights"):



        article_batches = list(self.generate_batch_sized_chunks(dataset[column_text], batch_size))
        target_batches = list(self.generate_batch_sized_chunks(dataset[column_summary], batch_size))


        for article_batch, target_batch in tqdm(zip(article_batches, target_batches), total=len(article_batches)):

                inputs = tokenizer(article_batch, max_length=1024,  truncation=True,
                                padding="max_length", return_tensors="pt")

                summaries = model.generate(input_ids=inputs["input_ids"].to(self.device),
                                attention_mask=inputs["attention_mask"].to(self.device),
                                length_penalty=0.8, num_beams=8, max_length=128)

                ''' parameter for length penalty ensures that the model does not generate sequences that are long '''

                decoded_summaries = [tokenizer.decode(s, skip_special_tokens=True,
                                        clean_up_tokenization_spaces=True)
                    for s in summaries]

                decoded_summaries = [d.replace("", " ") for d in decoded_summaries]

                metric.add_batch(predictions=decoded_summaries, references=target_batch)

        
        score = metric.compute()
        
        return score
    
    def evaluate_model(self):
        

        device = "cuda" if torch.cuda.is_available() else "cpu"


        rouge_metric = evaluate.load('rouge')

        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)

        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(self.device)

        
        dataset_samsum_pt = load_from_disk(self.config.data_path)


        rouge_names = ["rouge1", "rouge2", "rougeL", "rougeLsum"]

        # rouge_metric = rouge_metric

        score = self.calculate_metric_on_test_ds(dataset_samsum_pt['test'][0:10], rouge_metric, model, tokenizer, batch_size = 2, column_text = 'dialogue', column_summary= 'summary')

        
        rouge_dict = {rn:score[rn] for rn in rouge_names}

        df = pd.DataFrame(rouge_dict, index = [f'pegasus'])

        print("yes")
        

        df.to_csv("artifacts/model_evaluation/evaluation_results.csv", index=False)

        # df.to_csv(self.config.metric_full_name, index = False)


        