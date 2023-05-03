import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact')
def get_list():
    return {'name': 'Mike'}

@app.get('/html', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Hi, I am a h1 tag!</h1>
        <p>And I am a paragraph!</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()