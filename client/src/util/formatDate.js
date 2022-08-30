export const formatDate = (date) => {
  // format from yyyy-mm-dd to dd.mm.yyyy
  return date.split("-").reverse().join(".");
};
