#!/bin/bash

systemctl start ollama
ollama pull llama2
python3 main.py
