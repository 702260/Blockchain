FROM python: 3.6-alpine
WORkDIR /app

# Install depandencies
ADD requirements.txt /app
RUN cd /app && \ 
pip install -r requirements.txt

# Add actual source code

Add blockchain.py /app

EXPOSE 5000

CMD ["python", "blockchain.py", "--port", "5000"]








