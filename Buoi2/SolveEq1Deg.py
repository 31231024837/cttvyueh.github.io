{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b12cac44-1eae-4942-8179-c63e4b0c0883",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Nhập a:  1\n",
      "Nhập b:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.00x + 5.00 = 0: x = -5.00\n"
     ]
    }
   ],
   "source": [
    "# Nhập hệ số a, b\n",
    "a = float(input(\"Nhập a: \"))\n",
    "b = float(input(\"Nhập b: \"))\n",
    "\n",
    "# Hàm giải phương trình\n",
    "def solv1deg(a, b):\n",
    "    \"\"\"\n",
    "    Solve Equation ax + b = 0\n",
    "    Trả về:\n",
    "        nsol = -1  => vô số nghiệm\n",
    "        nsol = 0   => vô nghiệm\n",
    "        nsol = 1   => có 1 nghiệm duy nhất x\n",
    "    \"\"\"\n",
    "    nsol, x = None, None\n",
    "    if a == 0:\n",
    "        if b == 0:\n",
    "            nsol = -1   # vô số nghiệm\n",
    "        else:\n",
    "            nsol = 0    # vô nghiệm\n",
    "    else:\n",
    "        nsol = 1\n",
    "        x = -b / a\n",
    "    return nsol, x\n",
    "\n",
    "# Gọi hàm\n",
    "nsol, x = solv1deg(a, b)\n",
    "\n",
    "# Xuất kết quả\n",
    "if nsol == -1:\n",
    "    print(f\"{a:.2f}x + {b:.2f} = 0: unlimited solutions\")\n",
    "elif nsol == 0:\n",
    "    print(f\"{a:.2f}x + {b:.2f} = 0: no solution\")\n",
    "else:\n",
    "    print(f\"{a:.2f}x + {b:.2f} = 0: x = {x:.2f}\")"
   ]
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
