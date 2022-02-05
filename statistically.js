const percentCalc = (total, part) => part / total * 100;

//calculate statistically the possibility of n dice rolls in relation with the required roll (3 or more, 4 or more, etc)
const accerted = (amount, req_roll) => {
     return (amount / 100 * ((7 - req_roll) * (100 / 6)));
}

//console.log(acuracy(10, 3));

const setWoundReq = (weaponStrength, targetToughness) => {
    if (weaponStrength >= targetToughness * 2){
        return 2;
    }else if (weaponStrength > targetToughness){
        return 3;
    }else if (targetToughness >= weaponStrength * 2) {
        return 6;
    }else if (targetToughness > weaponStrength){
        return 5;
    }
    return 4;
}    

//console.log(setWoundReq(2, 4));

const setAllowedSave = (armorPen, armor) => {
    if (armorPen + armor > 6) {
        return false;
    }
    return armorPen + armor;
}

const takeAShot = (shots, bs, s, t, ap, save, woundPool) => {
    //to hit:
    const acuracy = accerted(shots, bs);
    //how much is needed to wound
    const reqToWound = setWoundReq(s, t);
    //from the hits how many wound
    const impactChecks = accerted(acuracy, reqToWound);
    //how much needed to save
    const allowedSave = setAllowedSave(ap, save);
    //saving throws
    if (allowedSave) {

        const totalDamage = accerted(impactChecks, allowedSave);
        return percentCalc(woundPool, totalDamage);
    } 
    return impactChecks;
}

//marines bolters to 10 firewarriors
console.log(takeAShot(10, 3, 4, 3, 1, 4, 10)); 

//fire warriors to 5 marines
console.log(takeAShot(20, 4, 5, 4, 0, 3, 10));