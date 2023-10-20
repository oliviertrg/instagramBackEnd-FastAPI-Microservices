FROM pypy:latest
# set the working directory
WORKDIR /work

EXPOSE 7780
# install dependencies
COPY ./requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install pydantic[email]
RUN pip install python-multipart
RUN pip install 'strawberry-graphql[fastapi]'



# copy the to the folder

COPY . ./

# start the server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7780", "--reload"]
