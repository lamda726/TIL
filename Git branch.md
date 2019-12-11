# Git branch

> Git 개발 흐름에서 branch는 매우 중요.
>
> 독립적인 개발환경을 제공하여 동시에 다양한 작업을 진행할 수 있도록 만들어준다.
>
> 일반적으로 브랜치의 이름은 해당 작업을 나타낸다.



## 1. 기초 명령어

```bash
$ git branch   # branch 목록 확인
$ git branch {브랜치이름} # {브랜치이름} 생성
$ git checkout {브랜치이름} # {브랜치이름}으로 이동
$ git branch -d {브랜치이름} # {브랜치이름} 삭제

$ git checkout -b {브랜치이름} # {브랜치이름} 생성 및 이동
```

* branch 병합

```bash
(master) $ git merge feature
# master 브랜치로 feature 브랜치 이력 가져오기 (병합)
```



### 상황 1. fast-foward

1. feature/test branch 생성 및 이동

   ```bash
   $ git checkout -b feature/test
   ```

2. 작업 완료 후 commit

   ```bash
   $ git test.txt
   $ git add .
   $ git commit -m 'test 기능 개발 완료'
   ae3cd40 (HEAD -> feature/test) test 기능 개발 완료
   adac551 (testbranch, master) Testbranch - test
   6a7b9ed (origin/master) 집 - a.txt 추가
   40c94ac 멀캠 - 작업
   338312f 집 - main.html
   ```


3. master 이동

   ```bash
   $ git checkout master
   ```
   
   ```bash
   $ git log --oneline
   adac551 (HEAD -> master, testbranch) Testbranch - test
   6a7b9ed (origin/master) 집 - a.txt 추가
   40c94ac 멀캠 - 작업
   338312f 집 - main.html
   e1afe6b 멀캠 - index.html
   ```


4. master에 병합

   ```bash
   $ git merge feature/test
   Updating adac551..ae3cd40
   Fast-forward
    test.txt | 0
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 test.txt
   ```


5. 결과 -> fast-foward (단순히 HEAD를 이동)

   ```bash
   $ git log --oneline
   ae3cd40 (HEAD -> master) test 기능 개발 완료
   adac551 (testbranch) Testbranch - test
   6a7b9ed (origin/master) 집 - a.txt 추가
   40c94ac 멀캠 - 작업
   338312f 집 - main.html
   e1afe6b 멀캠 - index.html
   ```

6. branch 삭제

   

   

---

### 상황 2. merge commit

> feature 브랜치에서 작업하고 있는 동안, master 브랜치에서 이력이 추가적으로 발생한 경우



1. feature/signout branch 생성 및 이동

   

2. 작업 완료 후 commit

   

3. master 이동

   

4. *master에 추가 commit 이 발생시키기!!*

   * **다른 파일을 수정 혹은 생성하세요!**

   

5. master에 병합

   

6. 결과 -> 자동으로 *merge commit 발생*

   

7. 그래프 확인하기

   ```bash
   $ git log --oneline --graph
   *   c0d35ad (HEAD -> master) Merge branch 'feature/signout'
   |\
   | * 546a3a6 (feature/signout) Complete signout
   * | e4b57a7 Update master
   |/
   * ae3cd40 test 기능 개발 완료
   * adac551 Testbranch - test
   * 6a7b9ed (origin/master) 집 - a.txt 추가
   * 40c94ac 멀캠 - 작업
   * 338312f 집 - main.html
   * e1afe6b 멀캠 - index.html
   ```

8. branch 삭제

   

---

### 상황 3. merge commit 충돌

1. feature/board branch 생성 및 이동

   ```bash
   $ git 
   ```

   

2. 작업 완료 후 commit

   ```bash
   # 직접 test.txt파일을 
   $ git add .
   ```
   
   


3. master 이동

   ```bash
   $ git checkout master
   ```
   
   


4. *master에 추가 commit 이 발생시키기!!*

   * **동일 파일을 수정 혹은 생성하세요!**

   ```bash
   # test.txt 수정
   $ git add .
   $ git commit -m 'master test'
   ```

5. master에 병합

   ```bash
   (master) $ git merge hotfix/test
   ```
   
   


6. 결과 -> *merge conflict발생*

   


7. 충돌 확인 및 해결

   <<<<<<< HEAD
   master 브랜치에서 수정
   우아아!
   
   hotfix 브랜치에서 수정
   우아아!
   
   >>>>>>> hotfix/test
   
   ```bash
   $ git status
   On branch master
   Your branch is ahead of 'origin/master' by 6 commits.
     (use "git push" to publish your local commits)
   
   You have unmerged paths.
     (fix conflicts and run "git commit")
     (use "git merge --abort" to abort the merge)
   
   Unmerged paths:
     (use "git add <file>..." to mark resolution)
           both modified:   test.txt
   
   no changes added to commit (use "git add" and/or "git commit -a")
   
   
   ```
   
   


8. merge commit 진행

    ```bash
    $ git add .
    $ git commit
$ git log --oneline
   511ed01 (HEAD -> master) Merge branch 'hotfix/test'
   030e276 master test
   f27943f (hotfix/test) hotfix test
   c0d35ad Merge branch 'feature/signout'
   e4b57a7 Update master
   546a3a6 (feature/signout) Complete signout
   ae3cd40 test 기능 개발 완료
   adac551 Testbranch - test
   6a7b9ed (origin/master) 집 - a.txt 추가
   40c94ac 멀캠 - 작업
   338312f 집 - main.html
   e1afe6b 멀캠 - index.html
   
   
   ```
   
   * vim 편집기 화면이 나타납니다.
   
   * 자동으로 작성된 커밋 메시지를 확인하고, `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료를 합니다.
      * `w` : write
      * `q` : quit
      
   * 커밋이  확인 해봅시다.
   
9. 그래프 확인하기

    


10. branch 삭제

    