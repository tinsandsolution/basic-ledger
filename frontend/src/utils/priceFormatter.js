export const makeProperPrice = (price) => {
    if (price.slice(-3) === ".00") return "$" + price.slice(0, -3)
    // let newPrice = firstPass(price)
    // if (newPrice[0] === "0") return newPrice[1]
    return "$" + price
}
