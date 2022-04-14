# hello

```
# build
docker build --rm --tag hello:v1 .

# run
docker run --rm --name test --detach --publish 5000:5000 hello:v1
```
