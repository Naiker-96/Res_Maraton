def gen_sec(n, m, a, c, x0):
  sec = []
  for i in range(n):
    sec.append((a * x0 + c) % m)
    x0 = sec[-1]
  return sec

def busqueda_bin(sec, x):
  ini = 0
  fin = len(sec) - 1
  while ini <= fin:
    mid = (ini + fin) // 2
    if sec[mid] == x:
      return True
    elif sec[mid] < x:
      ini = mid + 1
    else:
      fin = mid - 1
  return False

def contar_encontrados(sec):
  enc = set()
  for val in sec:
    if busqueda_bin(sec, val):
      enc.add(val)
  return len(enc)

n, m, a, c, x0 = map(int, input().split())

sec = gen_sec(n, m, a, c, x0)

resultado = contar_encontrados(sec)

print(resultado)
