# MLOps. Практическое задание №1 (vo-HW) и Итоговый проект

1) Создал репозиторий git, инфраструктуру для хранения артефактов в dvc, 2 ВМ в VirtualBox.
2) Установил и настроил необходимые ПО (VB, VScode, ssh-сервер, python, dvc и тд)
3) Установку необходимых библиотек python осуществил через requirements.txt
4) Построил модель, определил метрику, задал гиперпараметры, провел эксперимент, сохранил артефакты
5) Провел сравнение метрик
# Инфраструктура - виртуальные машины развернул в VBox:

1) Data-server - храним датасеты (DVC)
2) Admin-server - Jenkins и Ansible - с помощью этого сервера управляем остальными
3) ML-server - Обучение модели и push датасета  в Data-server с помощью DVC
В Jenkins запускается ansible playbook и проверяет есть ли измения гиперпараметра в репе, если да то мы мы переобучаем модель и сохраняем артефакт, а с помощью ansible можем управлять и datasrv и mlsrv
# Jenkins
![image](https://github.com/MaxAvgae/mlops2_project_1/assets/115181255/76a5aec8-bc9b-4233-904a-ba8950ebf985)
![image](https://github.com/MaxAvgae/mlops2_project_1/assets/115181255/44831ca2-fd96-46dd-b96c-50624b92d0c6)
![image](https://github.com/MaxAvgae/mlops2_project_1/assets/115181255/c7987405-301a-4cb9-b844-3ca9206a9e97)

# Вывод jenkins
04:50:30 Started by user Max Trokin
04:50:30 Running as SYSTEM
04:50:30 Building in workspace /var/lib/jenkins/workspace/test
04:50:30 The recommended git tool is: NONE
04:50:30 using credential ssh_jenk
04:50:30  > git rev-parse --resolve-git-dir /var/lib/jenkins/workspace/test/.git # timeout=10
04:50:30 Fetching changes from the remote Git repository
04:50:30  > git config remote.origin.url https://github.com/MaxAvgae/mlops2_project_1 # timeout=10
04:50:30 Fetching upstream changes from https://github.com/MaxAvgae/mlops2_project_1
04:50:30  > git --version # timeout=10
04:50:30  > git --version # 'git version 2.34.1'
04:50:30 using GIT_SSH to set credentials 
04:50:30 Verifying host key using known hosts file, will automatically accept unseen keys
04:50:30  > git fetch --tags --force --progress -- https://github.com/MaxAvgae/mlops2_project_1 +refs/heads/*:refs/remotes/origin/* # timeout=10
04:50:30  > git rev-parse refs/remotes/origin/main^{commit} # timeout=10
04:50:30 Checking out Revision 4e8205c0a500c8d9ff07d08002f6a47e6003415f (refs/remotes/origin/main)
04:50:30  > git config core.sparsecheckout # timeout=10
04:50:30  > git checkout -f 4e8205c0a500c8d9ff07d08002f6a47e6003415f # timeout=10
04:50:30 Commit message: "exp9"
04:50:30  > git rev-list --no-walk 4e8205c0a500c8d9ff07d08002f6a47e6003415f # timeout=10
04:50:30 [test] $ /bin/sh -xe /tmp/jenkins5466451697003880359.sh
04:50:30 + echo Hello World!
04:50:30 Hello World!
04:50:30 + echo /var/lib/jenkins/workspace/test
04:50:30 /var/lib/jenkins/workspace/test
04:50:30 + echo /var/lib/jenkins/workspace/test@tmp
04:50:30 /var/lib/jenkins/workspace/test@tmp
04:50:30 + echo /var/lib/jenkins
04:50:30 /var/lib/jenkins
04:50:30 + echo
04:50:30 
04:50:30 [test] $ /bin/sh -xe /tmp/jenkins15623113817128765826.sh
04:50:30 + ansible-playbook /var/lib/jenkins/workspace/test/mlsrv_playbook.yml -i /var/lib/jenkins/workspace/test/hosts.txt
04:50:30 
04:50:30 PLAY [Обновление Git и DVC] ****************************************************
04:50:30 
04:50:30 TASK [Gathering Facts] *********************************************************
04:50:32 [DEPRECATION WARNING]: Distribution ubuntu 22.04 on host mlserver should use 
04:50:32 /usr/bin/python3, but is using /usr/bin/python for backward compatibility with 
04:50:32 prior Ansible releases. A future Ansible release will default to using the 
04:50:32 discovered platform python for this host. See https://docs.ansible.com/ansible/
04:50:32 2.10/reference_appendices/interpreter_discovery.html for more information. This
04:50:32  feature will be removed in version 2.12. Deprecation warnings can be disabled 
04:50:32 by setting deprecation_warnings=False in ansible.cfg.
04:50:32 ok: [mlserver]
04:50:32 
04:50:32 TASK [Получить изменения из Git] ***********************************************
04:50:34 ok: [mlserver]
04:50:34 
04:50:34 TASK [Запустить DVC repro] *****************************************************
04:50:35 changed: [mlserver]
04:50:35 
04:50:35 TASK [Добавить и зафиксировать изменения в Git] ********************************
04:50:35 changed: [mlserver]
04:50:35 
04:50:35 TASK [Отправить в Git] *********************************************************
04:50:36 changed: [mlserver]
04:50:36 
04:50:36 TASK [Отправить в DVC] *********************************************************
04:50:37 changed: [mlserver]
04:50:38 
04:50:38 PLAY RECAP *********************************************************************
04:50:38 mlserver                   : ok=6    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
04:50:38 
04:50:38 Finished: SUCCESS
# Настроенные машины
![image](https://github.com/MaxAvgae/mlops2_project_1/assets/115181255/46352a7f-f1ca-45a9-94bb-2eca6595c519)
