/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    if(nums.length==0){
        return init;
    }
    i = 0 
    val = fn(init, nums[i])
    i+=1
    while(i<nums.length){
        val = fn(val, nums[i])
        i+=1;
    }
    return val;
};