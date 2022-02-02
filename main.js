
const test = () => {
    let unit = document.querySelector("#unitName").value;
    let weapon = document.querySelector("#weaponName").value;
    let target = document.querySelector("#target").value;

    let amount = Number.parseInt(document.querySelector("#amount").value);
    let bs = Number.parseInt(document.querySelector("#bs").value);
    let s = Number.parseInt(document.querySelector("#strength").value);
    let ap = Number.parseInt(document.querySelector("#armorPen").value);
    let t = Number.parseInt(document.querySelector("#toughness").value);
    let save = Number.parseInt(document.querySelector("#save").value);

    console.log(unit, weapon, target, typeof amount, bs, s, ap, t, save)
} 
