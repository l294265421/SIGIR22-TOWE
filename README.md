# Entire-Space-TOWE
Training Entire-Space Models for Target-oriented Opinion Words Extraction (SIGIR 2022)

# ARGCN
[code](https://github.com/l294265421/Entire-Space-TOWE-ARGCN)

# IOG

## Requirements
anaconda

Python==3.7.1

torch==1.2.0 

Keras==2.2.4 

tqdm==4.28.1 

dgl==0.3.1

jsonnet==0.14.0

allennlp==0.9.0 

overrides==3.1.0 

beautifulsoup4==4.6.3 

jieba==0.42.1 

psutil==5.4.8 

networkx==2.2

nltk==3.4

## pre-requisites
- Before excuting the following commands, replace glove.840B.300d.txt(http://nlp.stanford.edu/data/wordvecs/glove.840B.300d.zip), bert-base-uncased.tar.gz(https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased.tar.gz) and vocab.txt(https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased-vocab.txt) with the corresponding absolute paths in your computer.

- we prepare nltk_data at ./external_data/nltk_data.zip, please unzip it.

- install en_core_web_sm: pip install external_data/en_core_web_sm-2.1.0.tar.gz

## TOWE non-entire_space IOG (Training-validation instance type: Type I instance, Test instance type: Entire space)
sh repeat_non_bert.sh 0 iog-rest14-0,iog-rest14-1,iog-rest14-2,iog-rest14-3,iog-rest14-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath glove.840B.300d.txt  --current_dataset ASOTEDataRest14 --data_type iog --model_name IOG --train True --evaluate True --predict False --crf False --epochs 10 --batch_size 1 --entire_space False > towe.iog-rest14-0.log 2>&1 &

sh repeat_non_bert.sh 0 iog-lapt14-0,iog-lapt14-1,iog-lapt14-2,iog-lapt14-3,iog-lapt14-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath glove.840B.300d.txt  --current_dataset ASOTEDataLapt14 --data_type iog --model_name IOG --train True --evaluate True --predict False --crf False --epochs 10 --batch_size 1 --entire_space False > towe.iog-lapt14-0.log 2>&1 &

sh repeat_non_bert.sh 0 iog-rest15-0,iog-rest15-1,iog-rest15-2,iog-rest15-3,iog-rest15-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath glove.840B.300d.txt  --current_dataset ASOTEDataRest15 --data_type iog --model_name IOG --train True --evaluate True --predict False --crf False --epochs 10 --batch_size 1 --entire_space False > towe.iog-rest15-0.log 2>&1 &

sh repeat_non_bert.sh 0 iog-rest16-0,iog-rest16-1,iog-rest16-2,iog-rest16-3,iog-rest16-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath glove.840B.300d.txt  --current_dataset ASOTEDataRest16 --data_type iog --model_name IOG --train True --evaluate True --predict False --crf False --epochs 10 --batch_size 1 --entire_space False > towe.iog-rest16-0.log 2>&1 &

## TOWE non-non IOG (Training-validation instance type: Type I instance, Test instance type: Type I instance)
sh repeat_non_bert.sh 0 iog-rest14-0,iog-rest14-1,iog-rest14-2,iog-rest14-3,iog-rest14-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath glove.840B.300d.txt  --current_dataset ASOTEDataRest14 --data_type iog_non --model_name IOG --train True --evaluate True --predict False --crf False --epochs 10 --batch_size 1 --entire_space False --test_entire_space False > towe.iog-non-rest14-0.log 2>&1 &

sh repeat_non_bert.sh 0 iog-lapt14-0,iog-lapt14-1,iog-lapt14-2,iog-lapt14-3,iog-lapt14-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath glove.840B.300d.txt  --current_dataset ASOTEDataLapt14 --data_type iog_non --model_name IOG --train True --evaluate True --predict False --crf False --epochs 10 --batch_size 1 --entire_space False --test_entire_space False > towe.iog-non-lapt14-0.log 2>&1 &

sh repeat_non_bert.sh 0 iog-rest15-0,iog-rest15-1,iog-rest15-2,iog-rest15-3,iog-rest15-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath glove.840B.300d.txt  --current_dataset ASOTEDataRest15 --data_type iog_non --model_name IOG --train True --evaluate True --predict False --crf False --epochs 10 --batch_size 1 --entire_space False --test_entire_space False > towe.iog-non-rest15-0.log 2>&1 &

sh repeat_non_bert.sh 0 iog-rest16-0,iog-rest16-1,iog-rest16-2,iog-rest16-3,iog-rest16-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath glove.840B.300d.txt  --current_dataset ASOTEDataRest16 --data_type iog_non --model_name IOG --train True --evaluate True --predict False --crf False --epochs 10 --batch_size 1 --entire_space False --test_entire_space False > towe.iog-non-rest16-0.log 2>&1 &

## TOWE entire_space IOG (Training-validation instance type: Entire space, Test instance type: Entire space)
sh repeat_non_bert.sh 0 iog-rest14-0,iog-rest14-1,iog-rest14-2,iog-rest14-3,iog-rest14-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath glove.840B.300d.txt  --current_dataset ASOTEDataRest14 --data_type iog-entire_space --model_name IOG --train True --evaluate True --predict False --crf False --epochs 10 --batch_size 1 --entire_space True > towe.iog-rest14-0-entire_space.log 2>&1 &

sh repeat_non_bert.sh 0 iog-lapt14-0,iog-lapt14-1,iog-lapt14-2,iog-lapt14-3,iog-lapt14-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath glove.840B.300d.txt  --current_dataset ASOTEDataLapt14 --data_type iog-entire_space --model_name IOG --train True --evaluate True --predict False --crf False --epochs 10 --batch_size 1 --entire_space True > towe.iog-lapt14-0-entire_space.log 2>&1 &

sh repeat_non_bert.sh 0 iog-rest15-0,iog-rest15-1,iog-rest15-2,iog-rest15-3,iog-rest15-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath glove.840B.300d.txt  --current_dataset ASOTEDataRest15 --data_type iog-entire_space --model_name IOG --train True --evaluate True --predict False --crf False --epochs 10 --batch_size 1 --entire_space True > towe.iog-rest15-0-entire_space.log 2>&1 &

sh repeat_non_bert.sh 0 iog-rest16-0,iog-rest16-1,iog-rest16-2,iog-rest16-3,iog-rest16-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath glove.840B.300d.txt  --current_dataset ASOTEDataRest16 --data_type iog-entire_space --model_name IOG --train True --evaluate True --predict False --crf False --epochs 10 --batch_size 1 --entire_space True > towe.iog-rest16-0-entire_space.log 2>&1 &

## TOWE non-entire_space IOG+bert (Training-validation instance type: Type I instance, Test instance type: Entire space)
sh repeat_non_bert.sh 0 103-ASOTEDataRest14-0,103-ASOTEDataRest14-1,103-ASOTEDataRest14-2,103-ASOTEDataRest14-3,103-ASOTEDataRest14-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath  glove.840B.300d.txt --bert_file_path  bert-base-uncased.tar.gz --bert_vocab_file_path vocab.txt  --current_dataset ASOTEDataRest14 --data_type common_bert_with_second_sentence_103 --model_name TermBertWithSecondSentence --train True --evaluate True --predict False --crf False --same_special_token False --fixed_bert False --position_and_second_sentence False --entire_space False > towe.103-ASOTEDataRest14-0.log 2>&1

sh repeat_non_bert.sh 0 103-ASOTEDataLapt14-0,103-ASOTEDataLapt14-1,103-ASOTEDataLapt14-2,103-ASOTEDataLapt14-3,103-ASOTEDataLapt14-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath  glove.840B.300d.txt --bert_file_path  bert-base-uncased.tar.gz --bert_vocab_file_path vocab.txt  --current_dataset ASOTEDataLapt14 --data_type common_bert_with_second_sentence_103 --model_name TermBertWithSecondSentence --train True --evaluate True --predict False --crf False --same_special_token False --fixed_bert False --position_and_second_sentence False --entire_space False > towe.103-ASOTEDataLapt14-0.log 2>&1

sh repeat_non_bert.sh 0 103-ASOTEDataRest15-0,103-ASOTEDataRest15-1,103-ASOTEDataRest15-2,103-ASOTEDataRest15-3,103-ASOTEDataRest15-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath  glove.840B.300d.txt --bert_file_path  bert-base-uncased.tar.gz --bert_vocab_file_path vocab.txt  --current_dataset ASOTEDataRest15 --data_type common_bert_with_second_sentence_103 --model_name TermBertWithSecondSentence --train True --evaluate True --predict False --crf False --same_special_token False --fixed_bert False --position_and_second_sentence False --entire_space False > towe.103-ASOTEDataRest15-0.log 2>&1

sh repeat_non_bert.sh 0 103-ASOTEDataRest16-0,103-ASOTEDataRest16-1,103-ASOTEDataRest16-2,103-ASOTEDataRest16-3,103-ASOTEDataRest16-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath  glove.840B.300d.txt --bert_file_path  bert-base-uncased.tar.gz --bert_vocab_file_path vocab.txt  --current_dataset ASOTEDataRest16 --data_type common_bert_with_second_sentence_103 --model_name TermBertWithSecondSentence --train True --evaluate True --predict False --crf False --same_special_token False --fixed_bert False --position_and_second_sentence False --entire_space False > towe.103-ASOTEDataRest16-0.log 2>&1

## TOWE non-non IOG+bert (Training-validation instance type: Type I instance, Test instance type: Type I instance)
sh repeat_non_bert.sh 0 108-ASOTEDataRest14-0,108-ASOTEDataRest14-1,108-ASOTEDataRest14-2,108-ASOTEDataRest14-3,108-ASOTEDataRest14-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath  glove.840B.300d.txt --bert_file_path  bert-base-uncased.tar.gz --bert_vocab_file_path vocab.txt  --current_dataset ASOTEDataRest14 --data_type common_bert_with_second_sentence_108 --model_name TermBertWithSecondSentence --train True --evaluate True --predict False --crf False --same_special_token False --fixed_bert False --position_and_second_sentence False --entire_space False --test_entire_space False > towe.108-ASOTEDataRest14-0.log 2>&1

sh repeat_non_bert.sh 0 108-ASOTEDataLapt14-0,108-ASOTEDataLapt14-1,108-ASOTEDataLapt14-2,108-ASOTEDataLapt14-3,108-ASOTEDataLapt14-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath  glove.840B.300d.txt --bert_file_path  bert-base-uncased.tar.gz --bert_vocab_file_path vocab.txt  --current_dataset ASOTEDataLapt14 --data_type common_bert_with_second_sentence_108 --model_name TermBertWithSecondSentence --train True --evaluate True --predict False --crf False --same_special_token False --fixed_bert False --position_and_second_sentence False --entire_space False --test_entire_space False > towe.108-ASOTEDataLapt14-0.log 2>&1

sh repeat_non_bert.sh 0 108-ASOTEDataRest15-0,108-ASOTEDataRest15-1,108-ASOTEDataRest15-2,108-ASOTEDataRest15-3,108-ASOTEDataRest15-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath  glove.840B.300d.txt --bert_file_path  bert-base-uncased.tar.gz --bert_vocab_file_path vocab.txt  --current_dataset ASOTEDataRest15 --data_type common_bert_with_second_sentence_108 --model_name TermBertWithSecondSentence --train True --evaluate True --predict False --crf False --same_special_token False --fixed_bert False --position_and_second_sentence False --entire_space False --test_entire_space False > towe.108-ASOTEDataRest15-0.log 2>&1

sh repeat_non_bert.sh 0 108-ASOTEDataRest16-0,108-ASOTEDataRest16-1,108-ASOTEDataRest16-2,108-ASOTEDataRest16-3,108-ASOTEDataRest16-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath  glove.840B.300d.txt --bert_file_path  bert-base-uncased.tar.gz --bert_vocab_file_path vocab.txt  --current_dataset ASOTEDataRest16 --data_type common_bert_with_second_sentence_108 --model_name TermBertWithSecondSentence --train True --evaluate True --predict False --crf False --same_special_token False --fixed_bert False --position_and_second_sentence False --entire_space False --test_entire_space False > towe.108-ASOTEDataRest16-0.log 2>&1

## TOWE entire_space IOG+bert (Training-validation instance type: Entire space, Test instance type: Entire space)
sh repeat_non_bert.sh 0 104-ASOTEDataRest14-0,104-ASOTEDataRest14-1,104-ASOTEDataRest14-2,104-ASOTEDataRest14-3,104-ASOTEDataRest14-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath  glove.840B.300d.txt --bert_file_path  bert-base-uncased.tar.gz --bert_vocab_file_path vocab.txt  --current_dataset ASOTEDataRest14 --data_type common_bert_with_second_sentence_104 --model_name TermBertWithSecondSentence --train True --evaluate True --predict False --crf False --same_special_token False --fixed_bert False --position_and_second_sentence False --entire_space True > towe.104-ASOTEDataRest14-0.entire_space.log 2>&1

sh repeat_non_bert.sh 0 104-ASOTEDataLapt14-0,104-ASOTEDataLapt14-1,104-ASOTEDataLapt14-2,104-ASOTEDataLapt14-3,104-ASOTEDataLapt14-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath  glove.840B.300d.txt --bert_file_path  bert-base-uncased.tar.gz --bert_vocab_file_path vocab.txt  --current_dataset ASOTEDataLapt14 --data_type common_bert_with_second_sentence_104 --model_name TermBertWithSecondSentence --train True --evaluate True --predict False --crf False --same_special_token False --fixed_bert False --position_and_second_sentence False --entire_space True > towe.104-ASOTEDataLapt14-0.entire_space.log 2>&1

sh repeat_non_bert.sh 0 104-ASOTEDataRest15-0,104-ASOTEDataRest15-1,104-ASOTEDataRest15-2,104-ASOTEDataRest15-3,104-ASOTEDataRest15-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath  glove.840B.300d.txt --bert_file_path  bert-base-uncased.tar.gz --bert_vocab_file_path vocab.txt  --current_dataset ASOTEDataRest15 --data_type common_bert_with_second_sentence_104 --model_name TermBertWithSecondSentence --train True --evaluate True --predict False --crf False --same_special_token False --fixed_bert False --position_and_second_sentence False --entire_space True > towe.104-ASOTEDataRest15-0.entire_space.log 2>&1

sh repeat_non_bert.sh 0 104-ASOTEDataRest16-0,104-ASOTEDataRest16-1,104-ASOTEDataRest16-2,104-ASOTEDataRest16-3,104-ASOTEDataRest16-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath  glove.840B.300d.txt --bert_file_path  bert-base-uncased.tar.gz --bert_vocab_file_path vocab.txt  --current_dataset ASOTEDataRest16 --data_type common_bert_with_second_sentence_104 --model_name TermBertWithSecondSentence --train True --evaluate True --predict False --crf False --same_special_token False --fixed_bert False --position_and_second_sentence False --entire_space True > towe.104-ASOTEDataRest16-0.entire_space.log 2>&1

## TOWE entire_space-non IOG+bert  (Training-validation instance type: Entire space, Test instance type: Type I instance)
sh repeat_non_bert.sh 0 109-ASOTEDataRest14-0,109-ASOTEDataRest14-1,109-ASOTEDataRest14-2,109-ASOTEDataRest14-3,109-ASOTEDataRest14-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath  glove.840B.300d.txt --bert_file_path  bert-base-uncased.tar.gz --bert_vocab_file_path vocab.txt  --current_dataset ASOTEDataRest14 --data_type common_bert_with_second_sentence_109 --model_name TermBertWithSecondSentence --train True --evaluate True --predict False --crf False --same_special_token False --fixed_bert False --position_and_second_sentence False --entire_space False --only_test_non_entire_space True > towe.109-ASOTEDataRest14-0.log 2>&1

sh repeat_non_bert.sh 0 109-ASOTEDataLapt14-0,109-ASOTEDataLapt14-1,109-ASOTEDataLapt14-2,109-ASOTEDataLapt14-3,109-ASOTEDataLapt14-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath  glove.840B.300d.txt --bert_file_path  bert-base-uncased.tar.gz --bert_vocab_file_path vocab.txt  --current_dataset ASOTEDataLapt14 --data_type common_bert_with_second_sentence_109 --model_name TermBertWithSecondSentence --train True --evaluate True --predict False --crf False --same_special_token False --fixed_bert False --position_and_second_sentence False --entire_space False --only_test_non_entire_space True > towe.109-ASOTEDataLapt14-0.log 2>&1

sh repeat_non_bert.sh 0 109-ASOTEDataRest15-0,109-ASOTEDataRest15-1,109-ASOTEDataRest15-2,109-ASOTEDataRest15-3,109-ASOTEDataRest15-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath  glove.840B.300d.txt --bert_file_path  bert-base-uncased.tar.gz --bert_vocab_file_path vocab.txt  --current_dataset ASOTEDataRest15 --data_type common_bert_with_second_sentence_109 --model_name TermBertWithSecondSentence --train True --evaluate True --predict False --crf False --same_special_token False --fixed_bert False --position_and_second_sentence False --entire_space False --only_test_non_entire_space True > towe.109-ASOTEDataRest15-0.log 2>&1

sh repeat_non_bert.sh 0 109-ASOTEDataRest16-0,109-ASOTEDataRest16-1,109-ASOTEDataRest16-2,109-ASOTEDataRest16-3,109-ASOTEDataRest16-4 nlp_tasks/absa/mining_opinions/sequence_labeling/towe_bootstrap.py --embedding_filepath  glove.840B.300d.txt --bert_file_path  bert-base-uncased.tar.gz --bert_vocab_file_path vocab.txt  --current_dataset ASOTEDataRest16 --data_type common_bert_with_second_sentence_109 --model_name TermBertWithSecondSentence --train True --evaluate True --predict False --crf False --same_special_token False --fixed_bert False --position_and_second_sentence False --entire_space False --only_test_non_entire_space True > towe.109-ASOTEDataRest16-0.log 2>&1

## Citation
```
@inproceedings{10.1145/3477495.3531768,
    author = {Li, Yuncong and Wang, Fang and Zhong, Sheng-Hua},
    title = {Training Entire-Space Models for Target-Oriented Opinion Words Extraction},
    year = {2022},
    isbn = {9781450387323},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    url = {https://doi.org/10.1145/3477495.3531768},
    doi = {10.1145/3477495.3531768},
    abstract = {Target-oriented opinion words extraction (TOWE) is a subtask of aspect-based sentiment analysis (ABSA). Given a sentence and an aspect term occurring in the sentence, TOWE extracts the corresponding opinion words for the aspect term. TOWE has two types of instance. In the first type, aspect terms are associated with at least one opinion word, while in the second type, aspect terms do not have corresponding opinion words. However, previous researches trained and evaluated their models with only the first type of instance, resulting in a sample selection bias problem. Specifically, TOWE models were trained with only the first type of instance, while these models would be utilized to make inference on the entire space with both the first type of instance and the second type of instance. Thus, the generalization performance will be hurt. Moreover, the performance of these models on the first type of instance cannot reflect their performance on entire space. To validate the sample selection bias problem, four popular TOWE datasets containing only aspect terms associated with at least one opinion word are extended and additionally include aspect terms without corresponding opinion words. Experimental results on these datasets show that training TOWE models on entire space will significantly improve model performance and evaluating TOWE models only on the first type of instance will overestimate model performance.},
    booktitle = {Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval},
    pages = {1875–1879},
    numpages = {5},
    keywords = {sample selection bias, aspect-based sentiment analysis, target-oriented opinion words extraction},
    location = {Madrid, Spain},
    series = {SIGIR '22}
}
```