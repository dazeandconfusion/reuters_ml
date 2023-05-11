# Scalable Machine Learning System for Hierarchical Multi-Label Text Classification based on Reuters dataset

## Dataset
[The dataset](https://archive.ics.uci.edu/ml/datasets/reuters-21578+text+categorization+collection) used represents a collection of assembled and categorized news articles by Reuters Ltd. The provided link refers to the data formatted using the SGML Markup Language. However, the more proper format for the needed data is additionally presented via the [Hugging Face](https://huggingface.co/datasets/reuters21578/viewer/ModLewis/train) or [NLTK library](https://www.nltk.org/book/ch02.html).

## Task
### Objective
Design a scalable, maintainable, and efficient machine learning system that handles hierarchical multi-label text classification for a growing dataset of news articles. The system should utilize cloud-based resources, support MLOps practices, and provide an API for integration with other applications.
### Task Decomposition
1. Analyze the requirements for a machine learning system that classifies news articles into hierarchical topics and subtopics. Consider factors such as data volume, model complexity, latency, and scalability.
2. Design the overall architecture of the system, including data ingestion, storage, preprocessing, model training, evaluation, and deployment. Incorporate the use of cloud-based resources, such as Azure ML, to optimize for scalability and maintainability.
3. Plan the integration of MLOps practices within the system, including continuous integration, continuous deployment, automated testing, and model monitoring.
4. Develop an API design to enable other applications to interact with the deployed model and perform classification tasks.
5. Address any security, privacy, and compliance concerns associated with the system, such as data storage, access control, and model explainability.
6. Prepare a system design document that outlines the architectural decisions, components, data flow, and rationale behind your design choices. Include diagrams and illustrations to visualize the overall structure of the system.

### Deliverables
1. A detailed system design document that includes architectural decisions, components, data flow, and rationale for design choices.
2. Visual diagrams and illustrations to support the system design.

## Experiments
| Architecture                 | F1-samples | Precision-samples | Recall-samples |
|------------------------------|------------|-------------------|----------------|
| preproc+ TF-IDF + KNN        | 38.73%     | 38.9%             | 38.8%          |
| TF-IDF + KNN                 | 79.36%     | 80.68%            | 79.8%          |
| preproc + TF-IDF + LinearSVC | 85.96%     | 87.65%            | 85.84%         |
| TF-IDF + LinearSVC           | 86.3%      | 87.99%            | 86.16%         |
| TF-IDF + Catboost            | 83.27%     | 84.67%            | 83.25%         |
| TF-IDF + XGBoost             | 87.1%      | 88.14%            | 87.7%          |

Conducted experiments have shown that the best F1-samples result leads to `TF-IDF + XGBoost`. 
This model will further be used in the service development.