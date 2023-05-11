from pathlib import Path
from typing import List, Optional

import joblib
import yaml
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from xgboost import XGBClassifier

_PATH = Path(__file__).resolve().parent
with open(_PATH / "config.yaml") as f:
    _CONFIG = yaml.safe_load(f)

_DATA_PATH = _PATH / "models"


class Inference:
    _vectorizer: TfidfVectorizer
    _model: XGBClassifier
    _postprocessing: MultiLabelBinarizer

    def __init__(self):
        self._vectorizer = joblib.load(_DATA_PATH / _CONFIG["vectorizer"])
        self._model = joblib.load(_DATA_PATH / _CONFIG["model"])
        self._postprocessing = joblib.load(_DATA_PATH / _CONFIG["mlb"])

    def run(self, text: str) -> List[Optional[str]]:
        vectors = self._vectorizer.transform([text])
        predicts = self._model.predict(vectors)
        result = self._postprocessing.inverse_transform(predicts)[0]
        if not result:
            result = (None,)
        return result
