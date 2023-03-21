FROM python:3.11

RUN mkdir /app

WORKDIR /app

#Copy files to image
COPY requirements.txt ./requirements.txt
COPY Makefile ./Makefile
COPY Reddit_Data.csv ./Reddit_Data.csv
COPY train.py ./train.py
COPY inference.py ./inference.py
COPY app.py ./app.py
COPY model ./model
COPY vectorizer ./vectorizer
ADD static ./
ADD templates ./

# Installation of the dependecies
RUN make install

ENTRYPOINT ["python", "app.py"]
# ENTRYPOINT ["python", "-m", "http.server", "5000"]
# EXPOSE 5000

# ENTRYPOINT ["/bin/bash"]
