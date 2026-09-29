/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    var count = n;
    return function() {
        let b = count;
        count++;
        return b;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */