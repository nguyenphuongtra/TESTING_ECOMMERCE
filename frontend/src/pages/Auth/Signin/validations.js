import * as yup from "yup";

const validations = yup.object().shape({
  email: yup.string().email("Nhập email hợp lệ").required("Bắt buộc"),
  email: yup
    .string()
    .email("Email không hợp lệ")
    .required("Email là bắt buộc"),
  password: yup
    .string()
    // .min(10, "Parolanız en az 10 karakter olmalıdır.")
    .required()
    .min(5, "Mật khẩu phải có ít nhất 5 ký tự.")  // thanh đổi từ 8 ký tự sang 5 ký tự
    .required("Mật khẩu là bắt buộc"),
  passwordConfirm: yup
    .string()
    // .oneOf([yup.ref("password")], "Parolanız uyuşmuyor")
    .required()
    .oneOf([yup.ref("password")], "Mật khẩu xác nhận không khớp")
    .required("Xác nhận mật khẩu là bắt buộc"),
});

export default validations;