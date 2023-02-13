# leaflogistics
Leaf Logistics Take Home

To run the Flask API
1. Create a python virtual environment and install the needed requirements (or your prefered environment setup method)
2. run the Flask API with the main.py file. The endpoint is "/transpose"
3. You should be able to access the Flask API at http://127.0.0.1:5000/transpose
4. Here is an example request you can send
    - curl -d "[[1,2,3],[4,5,6],[7,8,9]]" -H "Content-Type: application/json" https://127.0.0.1:5000/transpose
