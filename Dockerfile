# Imagem Airflow
FROM apache/airflow:2.0.1

#COpia o requirements.txt
COPY requirements.txt /requirements.txt

# Upgrade o pip 
RUN pip install --user --upgrade pip

#Instala as libs do requirements.txt]
RUN pip install --no-cache-dir --user -r /requirements.txt