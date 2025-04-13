#!/bin/bash
echo "⏳ Waiting for DB to be ready..."
sleep 5
echo "📥 Loading CSV into database..."
python3 app/load_csv.py
