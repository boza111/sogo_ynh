<!--
Ohart ongi: README hau automatikoki sortu da <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>ri esker
EZ editatu eskuz.
-->

# SOGo YunoHost-erako

[![Integrazio maila](https://dash.yunohost.org/integration/sogo.svg)](https://ci-apps.yunohost.org/ci/apps/sogo/) ![Funtzionamendu egoera](https://ci-apps.yunohost.org/ci/badges/sogo.status.svg) ![Mantentze egoera](https://ci-apps.yunohost.org/ci/badges/sogo.maintain.svg)

[![Instalatu SOGo YunoHost-ekin](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=sogo)

*[Irakurri README hau beste hizkuntzatan.](./ALL_README.md)*

> *Pakete honek SOGo YunoHost zerbitzari batean azkar eta zailtasunik gabe instalatzea ahalbidetzen dizu.*  
> *YunoHost ez baduzu, kontsultatu [gida](https://yunohost.org/install) nola instalatu ikasteko.*

## Aurreikuspena

SOGo is an opensource groupware solution which has Webmail, a global address book and Calender and Contacts which can be synced via caldav or cardav.


**Paketatutako bertsioa:** 5.8.0~ynh5

**Demoa:** <https://demo.sogo.nu/SOGo/>
## Dokumentazioa eta baliabideak

- Aplikazioaren webgune ofiziala: <https://sogo.nu/>
- Administratzaileen dokumentazio ofiziala: <https://www.sogo.nu/support.html#/documentation>
- Jatorrizko aplikazioaren kode-gordailua: <https://github.com/inverse-inc/sogo>
- YunoHost Denda: <https://apps.yunohost.org/app/sogo>
- Eman errore baten berri: <https://github.com/YunoHost-Apps/sogo_ynh/issues>

## Garatzaileentzako informazioa

Bidali `pull request`a [`testing` abarrera](https://github.com/YunoHost-Apps/sogo_ynh/tree/testing).

`testing` abarra probatzeko, ondorengoa egin:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/sogo_ynh/tree/testing --debug
edo
sudo yunohost app upgrade sogo -u https://github.com/YunoHost-Apps/sogo_ynh/tree/testing --debug
```

**Informazio gehiago aplikazioaren paketatzeari buruz:** <https://yunohost.org/packaging_apps>
