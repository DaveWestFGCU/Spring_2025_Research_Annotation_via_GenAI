dataset = \
{
    "EmoEvent": {
        "id": "emoevent",
        "name": "Proof of Concept Subset",
        "source": "https://github.com/fmplaza/EmoEvent",
        "text_source": "tweet",
        "filetype": "tsv",
        "location": "local",
        "is_split": False,
        "label_format": "single",
        "relpath": "datasets/subset/EmoEvents_raw_subset_original_labels.csv",
        "abspath": "E:/Projects/PythonProject/Dataset_Labeling_via_GenAI/datasets/subset/EmoEvents_raw_subset_original_labels.csv",
        "unused_columns": ["id", "offensive"],
        "remap_columns": {"tweet": "text", "emotion": "labels", "event": "context"},
        "unlabeled_label": "others",
        "label_type": "emotion",
        "label_list": ["anger", "disgust", "fear", "joy", "sadness", "surprise"],
        "min_labelers": 3,
        "max_labelers": 3,
        "num_consensus": 2
    },


    "GoEmotions POC": {
        "id": "goemotions_6_single_poc",
        "source": "https://github.com/google-research/google-research/tree/master/goemotions",
        "paper": "https://arxiv.org/pdf/2005.00547",
        "text_source": "Reddit comment",
        "filetype": "csv",
        "location": "local",
        "is_split": False,
        "label_format": "single",
        "relpath": "datasets/goemotions/ekman_6_single_label/poc_subset/goemotions_6_single_poc.csv",
        "unused_columns": ["original labels", "source"],
        "remap_columns": {},
        "unlabeled_label": "",
        "label_type": "emotion",
        "label_list": ["anger", "disgust", "fear", "joy", "sadness", "surprise", "neutral"],
        "min_labelers": 3,
        "max_labelers": 5,
        "num_consensus": 2
    },


    "EmoEvent (Tokenized)" : {
        "id": "emoevent_en_tokenized",
        "source": "https://github.com/fmplaza/EmoEvent",
        "text_source": "tweet",
        "filetype": "tsv",
        "location": "local",
        "is_split": False,
        "label_format": "single",
        "relpath": "",
        "abspath": "",
        "unused_columns": ["id", "offensive"],
        "remap_columns": {"tweet": "text", "emotion":"labels", "event": "context"},
        "unlabeled_label": "others",
        "label_type": "emotion",
        "label_list": ["anger", "disgust", "fear", "joy", "sadness", "surprise"],
        "min_labelers": 3,
        "max_labelers": 3,
        "num_consensus": 2
    },


    "EmoEvent (Raw)" : {
        "id": "emoevent_en_raw",
        "source": "https://github.com/fmplaza/EmoEvent",
        "text_source": "tweet",
        "filetype": "tsv",
        "location": "local",
        "is_split": False,
        "label_format": "single",
        "relpath": "",
        "abspath": "",
        "unused_columns": ["id", "offensive"],
        "remap_columns": {"tweet":"text", "emotion":"labels", "event": "context"},
        "unlabeled_label": "others",
        "label_type": "emotion",
        "label_list": ["anger", "disgust", "fear", "joy", "sadness", "surprise"],
        "min_labelers": 3,
        "max_labelers": 3,
        "num_consensus": 2
    },


    "GoEmotions Ekman Single": {
        "id": "goemotions_ekman_single",
        "source": "https://github.com/google-research/google-research/tree/master/goemotions",
        "paper": "https://arxiv.org/pdf/2005.00547",
        "text_source": "Reddit comment",
        "filetype": "csv",
        "location": "local",
        "is_split": False,
        "label_format": "single",
        "relpath": "datasets/goemotions/ekman_6_single_label/go_emotions_merged_unified.csv",
        "unused_columns": ["original labels", "source"],
        "remap_columns": {},
        "unlabeled_label": "",
        "label_type": "emotion",
        "label_list": ["anger", "disgust", "fear", "joy", "sadness", "surprise", "neutral"],
        "min_labelers": 3,
        "max_labelers": 5,
        "num_consensus": 2
    },


    "enISEAR": {
        "id": "enisear",
        "source": "https://www.romanklinger.de/data-sets/",
        "text_source": "sentence",
        "filetype": "csv",
        "location": "local",
        "is_split": False,
        "label_format": "single",
        "relpath": "",
        "abspath": "",
        "unused_columns": ["Sentence_id", "Temporal_Distance", "Intensity", "Duration", "Gender", "City", "Country", "Worker_id", "Time", "Anger", "Disgust", "Fear", "Guilt", "Joy", "Sadness", "Shame"],
        "remap_columns": {"Sentence": "text", "Prior_Emotion": "labels"},
        "unlabeled_label": None,
        "label_type": "emotion",
        "label_list": ["Anger", "Disgust", "Fear", "Guilt", "Joy", "Sadness", "Shame"],
        "min_labelers": 3,
        "max_labelers": 3,
        "num_consensus": 2
    },


    "StackOverflow": {
        "id": "stackoverflow",
        "source": "https://github.com/collab-uniba/EmotionDatasetMSR18",
        "text_source": "Stack Overflow post",
        "filetype": "csv",
        "location": "local",
        "is_split": False,
        "label_format": "single",
        "relpath": "",
        "abspath": "",
        "unused_columns": ["Group", "Set", "Id", "Rater 1", "Rater 2", "Rater 3"],
        "remap_columns": {"Text": "text", "Gold Label": "labels"},
        "unlabeled_label": None,
        "label_type": "emotion",
        "label_list": ["ANGER", "FEAR", "JOY", "LOVE", "SADNESS", "SURPRISE"],
        "min_labelers": 3,
        "max_labelers": 3,
        "num_consensus": 2
    },
}
