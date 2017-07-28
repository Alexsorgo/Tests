<h3>Запуск APPIUM</h3>
чтобы запустить аппиум необходимо:
1. открыть терминал прописать “appium”
2. Открыть новое окно терминала и прописать “python path_to_directory/start.py"
3. Или же открыть проект в PyCarm и запустить тесты. Запуск из PyCharm можно произовдить файлами main.py для каждого проекта отдельно.
Для тестирование одного отдельного теста можно использовать файл feature.py, для этого необходимо скопировать необходимый тест в данный файл.

Тесты предусмотрены под конкретные модели телефонов.<br>
На данный момент Android - Nexus 5, iOS - новый iPad<br>
В файле Constants хранятся все переменные необходимые для тестов.<br>
<p>Аргументы принимаемые файлом запуска можно посмотреть следующим образом:<br>
В терминале необходимо запустить файл start.py с параметром '-h'</p>
<code>python path_to_directory/start.py -h</code>

<h3>УСТАНОВКА:</h3>

<p>https://github.com/appium/appium - git appium’a</p>
<p>Минимальный набор команд для установки:</p>
<p>/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"<br>
brew install node<br>
brew install libimobiledevice --HEAD<br>
brew install ideviceinstaller<br>
npm install -g ios-deploy<br>
npm install -g appium<br>
npm install -g appium-doctor<br>
brew install carthage<br>
export ANDROID_HOME=/Users/admin/Library/Android/sdk<br>
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_121.jdk/Contents/Home<br>
export PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$JAVA_HOME/bin:/Library/<br>
sudo pip install appium-python-client<br></p>

Для работы с iphone. необходимо открыть проект /usr/local/lib/node_modules/appium/node_modules/appium-xcuitest-driver/WebDriverAgent/WebDriverAgent.xcodeproj
В нем необходимо выставить bundleID = ua.com.csltd.webdriveragenrunner и провижен из CS группы под название appium
поставить подписи CS Team во всех элементах проекта.