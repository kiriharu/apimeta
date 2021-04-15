// From https://stackoverflow.com/questions/4810841/pretty-print-json-using-javascript
jsonDisplay = {

    jsonstring : '' ,
    outputDivID : 'shpretty',

    outputPretty: function (jsonstring) {
        jsonstring = jsonstring=='' ? jsonDisplay.jsonstring : jsonstring;
        // prettify spacing
        var pretty  = JSON.stringify(JSON.parse(jsonstring),null,2);
        // syntaxhighlight the pretty print version
        shpretty = jsonDisplay.syntaxHighlight(pretty);
        //output to a div
        // This could be a one liner with jQuery
        // - but not making assumptions about jQuery or other library being available.
        newDiv = document.createElement("pre");
        newDiv.innerHTML = shpretty;
        document.getElementById(jsonDisplay.outputDivID).appendChild(newDiv);
    },

    syntaxHighlight : function (json) {

        if (typeof json != 'string') {
            json = JSON.stringify(json, undefined, 2);
        }

        json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
        return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function (match) {
            var cls = 'number';
            if (/^"/.test(match)) {
                if (/:$/.test(match)) {
                  cls = 'key';
                } else {
                  cls = 'string';
                }
            } else if (/true|false/.test(match)) {
                cls = 'boolean';
            } else if (/null/.test(match)) {
                cls = 'null';
            }
            return '<span class="' + cls + '">' + match + '</span>';
        });
    }
}

async function fetchInfo() {
    // getting url from form
    let form = document.querySelector('#site-url');
    const url = `/info?url=${form.value}`
    const response = await fetch(url, {
        method: 'GET',
        mode: "cors",
        cache: 'no-cache',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    return response.text()
}

async function display() {
    let data = await fetchInfo();
    jsonDisplay.jsonstring = data;
    jsonDisplay.outputDivID = "output_div";
    jsonDisplay.outputPretty(data);
}

document.querySelector(".btn-primary").addEventListener('click', function (el){
    display();
});