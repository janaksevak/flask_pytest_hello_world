from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<body>
    <h1 id="myText">Hello Current World</h1>
    <button onclick="foo()" id="myButton">Go to New World</button>

    <script>
        let isNewWorld = false;
        function foo() {
            const text = document.getElementById("myText");
            const button = document.getElementById("myButton");

            if (isNewWorld) {
                text.innerText = "Hello Current World";
                button.innerText = "Go to New World";
            } else {
                text.innerText = "Hello New World";
                button.innerText = "Go to Old World";
            }

            isNewWorld = !isNewWorld;
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
