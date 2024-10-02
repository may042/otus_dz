"""
Main pipeline for the project
"""

import os, sys
import joblib
print(os.listdir())
sys.path.append('../ДЗ')

from loguru import logger

from src.preprocessing import load_data, split_data
from src.train import train_model, evaluate_model




def main() -> None:
    logger.info("-----------------")
    logger.info("Starting pipeline")
    logger.info("Loading data")
    df = load_data()

    logger.info("Splitting data")
    train, test = split_data(df)

    logger.info("Training model")
    model = train_model(train)

    logger.info("Saving model")
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, os.path.join("models", "model_in_docker.joblib"))

    logger.info("Evaluating model")
    accuracy = evaluate_model(model, test)
    logger.info(f"Model accuracy / roc_auc / avg_prc : {accuracy}")

    logger.info("Pipeline complete")


if __name__ == "__main__":
    main()