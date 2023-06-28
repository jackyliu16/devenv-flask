import { Button } from 'antd';
import 'antd/dist/antd.css';
import { DrawScene, MarkerDraw } from 'bmap-draw';
import { createRef, useEffect, useState } from 'react';

const mapRef = createRef();

const Demo = () => {
    const [sceneDrawStatus, setDrawStatus] = useState(null);
    const [scene, setScene] = useState(null);
    useEffect(() => {
        const map = new BMapGL.Map(mapRef.current);
        map.centerAndZoom(new BMapGL.Point(116.291, 39.993), 13);
        map.setMapStyleV2({ styleJson: customStyleJSON });
        map.enableScrollWheelZoom();

        const scene = new DrawScene(map);
        const marker = new MarkerDraw(scene, {
            isOpen: true,
            isSeries: true,
            enableDragging: true,
            baseOpts: {}
        });
        setDrawStatus(marker);
        setScene(scene);
    }, []);
    return (
        <div>
            <div style={{ padding: 8 }}>
                <Button onClick={() => sceneDrawStatus.open()}>开启</Button>
                <Button onClick={() => sceneDrawStatus.close()}>禁用</Button>
                <Button onClick={() => scene.clearData()}>清除</Button>
            </div>
            <div ref={mapRef} style={{ width: 'auto', height: 450, position: 'relative' }} />
        </div>
    );
};

export default Demo;