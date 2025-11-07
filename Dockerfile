FROM python:3.12

WORKDIR /workspace
COPY requirements.txt /workspace/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /workspace

ENV PYTHONPATH=/workspace/src
CMD [ "bash" ]
