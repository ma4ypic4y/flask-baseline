docker exec -it flask-hello_flask_1 bash


docker exec -it -d58661b4adbe python trainmodel.py



curl --header "Content-Type: application/json" \
--request POST \
--data '{"flower":"1,2,3,7"}' \
http://localhost:5000/iris_post






