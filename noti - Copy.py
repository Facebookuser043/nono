import requests

response = requests.post("https://hook.eu2.make.com/ky7ae7ei7v067ey9dkwmxsi8khx5yter", json={
    "userId": 1,
    "title": "Megdad Can Do it, I guess!",
    "completed": False
}, headers={
    "Content-type": "application/json; charset=UTF-8"
})
