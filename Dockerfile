FROM python:3.11
RUN mkdir /app
WORKDIR /app
COPY requirements.txt ./requirements.txt
COPY Makefile ./Makefile
COPY Reddit_Data.csv ./Reddit_Data.csv
COPY train.py ./train.py
COPY inference.py ./inference.py
COPY app.py ./app.py
COPY model ./model
COPY vectorizer ./vectorizer
# Installation of the dependecies
RUN make install
CMD ["python3", "app.py"]
EXPOSE 5000

ENTRYPOINT ["/bin/bash"]