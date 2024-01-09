#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let j = 0;
  while ((len - j) > 0) {
    const tmp = list[len];
    list[len] = list[j];
    list[j] = tmp;
    j++;
    len--;
  }
  return list;
};
