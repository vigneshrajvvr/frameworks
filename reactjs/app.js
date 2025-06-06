const heading = React.createElement("h1", {id : "heading"}, "Hello World from React");

console.log(heading);

const parent = React.createElement("div", {id : "parent"}, 
    [React.createElement("div", {id : "child"}, 
        [
            React.createElement("h1",{}, "I'm an h1 tag"),
            React.createElement("h1",{}, "I'm an h1 tag")
        ]),
    React.createElement("div", {id : "child"}, 
        [
            React.createElement("h1",{}, "I'm an h1 tag"),
            React.createElement("h1",{}, "I'm an h1 tag")
        ])])

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(parent);