const foo = {
    x: 2,
    bar: () => console.log(this.x)
}
console.log(foo['bar']())