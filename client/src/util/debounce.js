export const debounce = (f, ms) => {
  let timer = null;

  return (...args) => {
    if (timer) clearTimeout(timer);
    timer = setTimeout(() => f(...args), ms);
  };
};
