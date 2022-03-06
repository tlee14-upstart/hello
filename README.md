# hello

```
# build
docker build --rm --tag hello:v1 .

# run
docker run --rm --name test --detach --publish 5001:5001 hello:v1
```
