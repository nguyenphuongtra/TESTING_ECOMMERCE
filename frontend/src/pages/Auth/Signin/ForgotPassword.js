import React, { useState } from "react";
import {
  Flex,
  Box,
  Heading,
  FormControl,
  FormLabel,
  Input,
  Button,
  Alert,
} from "@chakra-ui/react";

function ForgotPassword() {
  const [email, setEmail] = useState("");
  const [submitted, setSubmitted] = useState(false);
  const [errorEmail, setErrorEmail] = useState("");         // Thêm state để lưu lỗi email

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!email) {
      setErrorEmail("Email is required");          // Nếu email rỗng thì báo lỗi
      return;
    } else {
      setErrorEmail("");
    }
    // Logic xử lý gửi email reset mật khẩu
    setSubmitted(true);
  };

  return (
    <Flex align="center" width="full" justifyContent="center">
      <Box pt={10}>
        <Box textAlign="center">
          <Heading>Forgot Password</Heading>
        </Box>
        {submitted ? (
          <Alert status="success" mt={5}>
            Instructions to reset your password have been sent to {email}.   
          </Alert>
        ) : (
          <Box my={5} textAlign="left">
            <form onSubmit={handleSubmit}>
              <FormControl isInvalid={!!errorEmail}>
                <FormLabel>E-mail</FormLabel>
                <Input
                  name="email"
                  type="email"
                  placeholder="Enter your email"
                  value={email}
                  onChange={(e) => {
                    setEmail(e.target.value);
                    if (e.target.value) setErrorEmail("");   // Xóa lỗi khi người dùng nhập lại
                  }}
                />
                {errorEmail && (
                  <Box color="red.500" fontSize="sm" mt={1}>
                    {errorEmail}
                  </Box>
                )}
              </FormControl>
              <Button mt="4" width="full" type="submit" colorScheme="teal">
                Send Instructions 
              </Button>
            </form>
          </Box>
        )}
      </Box>
    </Flex>
  );
}

export default ForgotPassword;