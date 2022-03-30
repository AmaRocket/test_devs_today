
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/31?style=plastic">

# Newsboard test task

**Backend Dependencies/Packages
Create a virtualenv for Python 3
1.Head over to the terminal and run:**
```
virtualenv env 
```
**Replace env wih the actual name you want to give your Python virtual environment.
2.Activate the virtualenv**
```
source env/bin/activate
```

<h3>First we need to install all libraries
</h3>

```
!pip install -r requirements.txt
```

<h3>NewsBoardAPI is located on</h3>
```
http://localhost:8000/api/
```

<h3> Start docker container</h3>

```
docker-compose up
```


<h3>Heroku</h3>
<h4>Posts:</h4>
```
https://testnewsboard.herokuapp.com/api/posts/
```
<h4>Comments</h4>
```
https://testnewsboard.herokuapp.com/api/comments/
```
<h4>Authors</h4>
```
https://testnewsboard.herokuapp.com/api/authors/
```
<h4>Upvotes</h4>
```
https://testnewsboard.herokuapp.com/api/upvotes/<int:pk>
```

<h3>Postman collections</h3>
```
https://www.getpostman.com/collections/42c66306badeb35d2bf9
```
