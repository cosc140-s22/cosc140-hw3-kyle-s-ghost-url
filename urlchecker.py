#######################################################
#
# COSC 140 Homework 3: URL checker
#
#######################################################

def urlchecker(url):
  # begins with http or https
  if not (url.startswith('http://') or url.startswith('https://')):
    return False
  
  # split ://
  scheme,hostname = url.split("://")
  
  # at least one /
  sc = hostname.count("/")
  if sc < 1:
    return False
  
  # at most one ?
  qc = hostname.count("?")
  if qc > 1:
    return False
  
  # at most one #
  hc = hostname.count("#")
  if hc > 1:
    return False
  
  # no spaces
  if ' ' in url:
    return False
  
  # hash must go before question
  q = hostname.find("?")
  h = hostname.find("#")
  if q<h and h>0 and q>0:
    return False
  
  # check if hostname is empty
  if not hostname:
    return False
  
  # split at first backlash and look at hostname
  c = hostname.split("/")
  
  # check if there is only one colon
  hcolon = hostname.count(":")
  colon = c[0].count(":")
  if colon > 1:
    return False
  elif colon == 1:
    h,p = c[0].split(":")
    if hcolon > 1:
      return False
  elif hcolon > 0:
    return False
  
  # check if port is digits
    if not p.isdigit():
      return False
  
  return True

def testurl():
    urls = [ # valid
      ['https://example.com/', True],
      ['http://example.com/', True],
      ['http://example.com/?query', True],
      ['http://example.com/#fragment', True],
      ['http://example/', True],
      ['http://example/path/', True],
      ['http://example/path', True],
      ['https://example.com:3000/path#fragment?query', True],
      ['https://example.com/path#fragment?query', True],
      # invalid
      ['htt://example/', False],
      ['httpss://example/', False],
      ['https://example/:3000', False],
      ['https://example/?:3000?', False],
      ['https://example/?:3000#', False],
      ['https://example/xy z', False],
      ['https://example/xyz:', False],
      ['https://example', False],
    ]
    for url,expected in urls:
        if urlchecker(url) != expected:
            print(f"{url} is not valid, but your function claimed the opposite")
        else:
            print(f"{url} - ok")
testurl()
