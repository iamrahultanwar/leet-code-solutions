/**
 * @param {number[]} prices
 * @return {number}
 */

const maxNum = (a,b) => a > b ? a : b;
var maxProfit = function(prices) {
   let left = 0;
    let right = 0;
    let maxPrice = 0;
    for(right = 1;right<prices.length;right++) {
        if(prices[right] < prices[left]) {
            left = right;
        }
        maxPrice = maxNum(maxPrice,prices[right]- prices[left])
    }
    return maxPrice;
}