FROM python:latest

WORKDIR /usr/src/cnw

COPY ./req.txt /usr/src/req.txt
RUN pip install --upgrade pip
RUN pip install -r /usr/src/req.txt
RUN pip install jinja2

COPY . usr/src/cnw

EXPOSE 8000

# CMD ["uvicorn", "usr.src.cnw.main:app", "--host=0.0.0.0", "--reload"]
