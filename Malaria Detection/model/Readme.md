In this notebook, I will build a Convolution Neural Network ML Model that will be able to predict with a certain amount of accuracy whether or not an image of a cell has been infected with Malaria or not.

Diagnosis of malaria can be difficult:

Where malaria is not endemic any more (such as in the United States), health-care providers may not be familiar with the disease. Clinicians seeing a malaria patient may forget to consider malaria among the potential diagnoses and not order the needed diagnostic tests. Laboratorians may lack experience with malaria and fail to detect parasites when examining blood smears under the microscope.

Malaria is an acute febrile illness. In a non-immune individual, symptoms usually appear 10–15 days after the infective mosquito bite. The first symptoms – fever, headache, and chills – may be mild and difficult to recognize as malaria. If not treated within 24 hours, P. falciparum malaria can progress to severe illness, often leading to death.
Microscopic Diagnosis

Malaria parasites can be identified by examining under the microscope a drop of the patient’s blood, spread out as a “blood smear” on a microscope slide. Prior to examination, the specimen is stained to give the parasites a distinctive appearance. This technique remains the gold standard for laboratory confirmation of malaria. However, it depends on the quality of the reagents, of the microscope, and on the experience of the laboratorian.

Building a custom built 2-layered Convolution Neural Network provided fairly good results at 95% accuracy. F1 Score, Precision, and Recall were also at 95% for each giving us an equal and moderately low number of False Positives and False Negatives.

'ACCURACY SCORE:'
0.9508345428156749
'CLASSIFICATION REPORT:'
              precision    recall  f1-score   support

           0       0.95      0.95      0.95      2730
           1       0.95      0.95      0.95      2782

   micro avg       0.95      0.95      0.95      5512
   macro avg       0.95      0.95      0.95      5512
weighted avg       0.95      0.95      0.95      5512
Our transfer learned model using VGG16 as our base model did not perform as well with an accuracy level at 91% and much more False Negatives than False Positives (a lower precision when stating if the cell was not infected with Malaria) which is very dangerous in medical diagnoses. This is to be expected since the classification of such images is so highly specific, building a custom built model would give much better accuracy.