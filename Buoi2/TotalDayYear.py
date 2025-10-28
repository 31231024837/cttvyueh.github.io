{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "412a7bc0-4365-4ac0-a28a-8961e73a623f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Input\n",
    "y = int(input(\"Nhập năm: \"))\n",
    "\n",
    "# Hàm kiểm tra năm nhuận\n",
    "def isleap(y):\n",
    "    ans = False\n",
    "    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):\n",
    "        ans = True\n",
    "    return ans\n",
    "# end isleap\n",
    "\n",
    "# Hàm tính số ngày trong năm\n",
    "def daysyear(y):\n",
    "    ans = 365\n",
    "    if isleap(y):\n",
    "        ans = 366\n",
    "    return ans\n",
    "# end daysyear\n",
    "\n",
    "# Gọi hàm\n",
    "ans = daysyear(y)\n",
    "\n",
    "# Output\n",
    "print(f\"{ans}\")"
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
