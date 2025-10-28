{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "0ec12a8a-3ef0-41b3-9980-f8f876060559",
   "metadata": {},
   "source": [
    "# Sắp xếp "
   ]
  },
  {
   "cell_type": "raw",
   "id": "637f30e8-35de-4509-9401-b9c8a5fd2c84",
   "metadata": {},
   "source": [
    "Cho ba số nguyên a, b, c. Hãy sắp xếp ba số nguyên theo thứ tự tăng dần. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5f9dff21-2346-48cd-9032-c90d0450d258",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Nhập a:  4\n",
      "Nhập b:  2\n",
      "Nhập c:  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2 3 4\n"
     ]
    }
   ],
   "source": [
    "# Input a, b, c\n",
    "a = int(input(\"Nhập a: \"))\n",
    "b = int(input(\"Nhập b: \"))\n",
    "c = int(input(\"Nhập c: \"))\n",
    "\n",
    "# Hàm hoán đổi để sắp xếp 3 số tăng dần\n",
    "def sort3(a, b, c):\n",
    "    # nếu a > b thì đổi chỗ\n",
    "    if a > b:\n",
    "        a, b = b, a\n",
    "    # nếu a > c thì đổi chỗ\n",
    "    if a > c:\n",
    "        a, c = c, a\n",
    "    # nếu b > c thì đổi chỗ\n",
    "    if b > c:\n",
    "        b, c = c, b\n",
    "    return a, b, c\n",
    "\n",
    "# Gọi hàm sắp xếp\n",
    "a, b, c = sort3(a, b, c)\n",
    "\n",
    "# Output\n",
    "print(a, b, c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f591b88-a065-46ed-ac3b-3f4ec2466ffa",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
