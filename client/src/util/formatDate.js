export const formatDate = (date) => {
  // format from yyyy-mm-dd to dd.mm.yyyy
  return date.split("-").reverse().join(".");
};

export const unformatDate = (date) => {
  // format from dd.mm.yyyy to yyyy-mm-dd
  return date.split(".").reverse().join("-");
};
