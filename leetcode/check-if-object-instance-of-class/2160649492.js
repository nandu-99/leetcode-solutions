/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (obj === null || obj === undefined || typeof classFunction !== "function") {
        return false;
    }

    let current = Object.getPrototypeOf(obj);

    while (current !== null) {
        if (current === classFunction.prototype) {
            return true;
        }
        current = Object.getPrototypeOf(current);
    }

    return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */