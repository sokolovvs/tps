#!/bin/bash

pathToTrainedModel="model"

echo "Check that trained file $pathToTrainedModel model is exists"
if [[ ! -f "$pathToTrainedModel" ]]; then
  echo "Model is not exists. You should add a trained model in project's root. Exit."
  exit 1
fi
echo "Ok. File $pathToTrainedModel is exists"
