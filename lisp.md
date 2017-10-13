## 程序描述

1. 坐标展点：读取坐标文本文件，标出点位与点号，高程（属性块）
2. 坐标解算：内外插点法（捕捉两个已知点，输入与第一个点的距离）
3. 坐标解算：直角坐标法（捕捉两个已知点，输入与第一个点的距离以及到连线的垂距
4. 坐标解算：距离交汇法（捕捉两个已知点，输入两个距离）

## 实现

1.
```Common Lisp
(defun c:plot_point () ;;;坐标展点
  (if (not (tblsearch "block" "block_point"))
  (write_block))
  (setq osmode_old (getvar "osmode"))
  (setvar "osmode" 0)
  (setvar "attdia" 0)  ;;;设定块的属性由命令行输入
  (setq file (getfiled "选定点位数据文件" "d:/" "txt" 0))
  (setq f (open file "r"))
  (setq pl nil)
  (setq s (read-line f))
  (while (/= s "000")
    (setq pn (atoi (substr s 17 4)))
    (setq x (atof (substr s 37 10)))
    (setq y (atof (substr s 21 10)))
    (setq h (atof (substr s 53 10)) h (rtos h 2 2))
    (command "_insert" "block_point" (list x y) 1 1 0 pn h "")
    (setq s (read-line f))
)

   (setvar "osmode" osmode_old)
  )

(defun write_block () ;;;创建一个名为block_point的块
  (command "_attdef" "" "No" "点号" "" '(1 0.5) 1 "")
  (setq e1 (entlast))
  (command "_attdef" "" "Height" "高程" "" '(1 -1.5) 1 "")
  (command "line" '(1 0) '(5 0) "")
  (command "point" '(0 0))
  (setq e2 (entnext e1) e3 (entnext e2) e4 (entnext e3))
  (setq ss (ssadd))
  (ssadd e1 ss)
  (ssadd e2 ss)
  (ssadd e3 ss)
  (ssadd e4 ss)
  (command "_block" "block_point" '(0 0) ss "") 
  )
  ```
  2. 