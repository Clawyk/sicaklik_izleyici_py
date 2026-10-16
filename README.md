# Sıcaklık İzleyici

ROS 2 ve Python kullanılarak geliştirilen sıcaklık izleme uygulaması.

#Gereksinimler

- Ubuntu 26.04
- ROS 2 Lyrical
- Python 3
- colcon

# Özellikler

- Sensör düğümü 20-40°C arasında rastgele sıcaklık üretiyor.
- Sıcaklık değerleri `/sicaklik` konusu üzerinden `Float32` mesajı olarak yayınlanır.
- İzleyici düğümü sıcaklıkları ekrana yazdırır.
- Sıcaklık 30°C'yi aştığında uyarı verir.

# Kurulum

```
cd ~/ros2_ws
colcon build --packages-select sicaklik_izleyici_py
source /opt/ros/lyrical/setup.bash
source ~/ros2_ws/install/setup.bash
```

# Çalıştırma

Birinci terminalde sensörü başlatın:


source /opt/ros/lyrical/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 run sicaklik_izleyici_py sensor


İkinci terminalde izleyiciyi başlatın:

```

source /opt/ros/lyrical/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 run sicaklik_izleyici_py izleyici
```

# Düğüm Grafiği

Üçüncü terminalde:

```
source /opt/ros/lyrical/setup.bash
ros2 run rqt_graph rqt_graph
```

Düğüm grafiği ekran görüntüsü teslim dosyalarına eklenmiştir.
